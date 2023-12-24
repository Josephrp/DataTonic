import torchaudio
import torch
import os
import time
import soundfile as sf
import json
import os
import asyncio
import streamlit as st
from src.module.semantic_kernel_module import SemanticKernelDataModule
from src.module.taskweaver_module import TaskWeaverDataProcessor
from src.module.autogen_module import AutoGenModule

def process_image(image, project_id, region, access_token):
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    request_body = {
        "contents": {
            "role": "user",
            "parts": [
                {
                    "fileData": {
                        "mimeType": "image/jpeg",
                        "data": img_str
                    }
                },
                {
                    "text": "Describe this picture from the perspective of SoW on the topic of the picture. use titles and subtitles to produce a complete statement of work based on the picture provided."
                }
            ]
        },
        "safety_settings": {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_LOW_AND_ABOVE"
        },
        "generation_config": {
            "temperature": 0.4,
            "topP": 1.0,
            "topK": 32,
            "maxOutputTokens": 2048
        }
    }
    endpoint = f"https://{region}-aiplatform.googleapis.com/v1/projects/{project_id}/locations/{region}/publishers/google/models/gemini-pro-vision:streamGenerateContent"
    response = requests.post(endpoint, headers={"Authorization": f"Bearer {access_token}"}, json=request_body)
    return response.json()

def save_and_resample_audio(input_audio_path, output_audio_path, resample_rate=16000):
    waveform, sample_rate = torchaudio.load(input_audio_path)

    resampler = torchaudio.transforms.Resample(sample_rate, resample_rate, dtype=waveform.dtype)
    resampled_waveform = resampler(waveform)

    torchaudio.save(output_audio_path, resampled_waveform, resample_rate)

def save_audio(audio_input, output_dir="saved_audio", resample_rate=16000):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    sample_rate, audio_data = audio_input
    file_name = f"audio_{int(time.time())}.wav"
    file_path = os.path.join(output_dir, file_name)
    sf.write(file_path, audio_data, sample_rate)

    resampled_file_path = os.path.join(output_dir, f"resampled_{file_name}")
    save_and_resample_audio(file_path, resampled_file_path, resample_rate)

    return resampled_file_path

def speech_to_text(audio_data, tgt_lang):
    file_path = save_audio(audio_data)
    audio_input, _ = torchaudio.load(file_path)
    s2t_model = torch.jit.load("unity_on_device.ptl", map_location=torch.device('cpu'))
    with torch.no_grad():
        model_output = s2t_model(audio_input, tgt_lang=languages[tgt_lang])
    transcribed_text = model_output[0] if model_output else ""
    print("Speech to Text Model Output:", transcribed_text)

    return transcribed_text

def speech_to_speech_translation(audio_data, tgt_lang):
    file_path = save_audio(audio_data)
    audio_input, _ = torchaudio.load(file_path)
    s2st_model = torch.jit.load("unity_on_device.ptl", map_location=torch.device('cpu'))
    with torch.no_grad():
        translated_text, units, waveform = s2st_model(audio_input, tgt_lang=languages[tgt_lang])
    output_file = "/tmp/result.wav"
    torchaudio.save(output_file, waveform.unsqueeze(0), sample_rate=16000)
    print("Translated Text:", translated_text)
    print("Units:", units)
    print("Waveform Shape:", waveform.shape)

    return translated_text, output_file


async def process_user_input(user_input):
    semantic_kernel = SemanticKernelDataModule()
    taskweaver = TaskWeaverDataProcessor()
    autogen_module = AutoGenModule(memgpt_memory_path="./src/autogen/MemGPT", openai_api_key=os.getenv('OPENAI_API_KEY'))
    
    autogen_module.semantic_kernel = semantic_kernel
    autogen_module.taskweaver = taskweaver
    
    sow_document = await semantic_kernel.create_and_fetch_sow(user_input)
    
    executed_plan = await autogen_module.AutoGenModule(sow_document)
    
    return executed_plan


async def process_user_input(user_input):
    semantic_kernel = SemanticKernelDataModule()
    taskweaver = TaskWeaverDataProcessor()
    autogen_module = AutoGenModule(memgpt_memory_path="./src/autogen/MemGPT", openai_api_key=os.getenv('OPENAI_API_KEY'))
    
    autogen_module.semantic_kernel = semantic_kernel
    autogen_module.taskweaver = taskweaver
    
    sow_document = await semantic_kernel.create_and_fetch_sow(user_input)
    
    executed_plan = await autogen_module.AutoGenModule(sow_document)
    
    return executed_plan

# @cl.on_chat_start
# async def start():
#     # Initial setup if needed
#     pass

# @cl.on_message
# async def main(message: cl.Message):
#     user_input = message.content
#     executed_plan = await process_user_input(user_input)
    
#     # Assuming the executed_plan is a string or something that can be converted to a string
#     await cl.Message(content=str(executed_plan)).send()

# # Streamlit app
# def main():
#     st.title("DataTonic")
#     st.subheader("🌟DataTonic: A Data-Capable AGI-style Agent Builder of Agents")

#     # User input text
#     user_input = st.text_area("Describe your request in detail with objectives and how you might achieve it:")

#     # Language selection for speech-to-text
#     languages = {
#         "English": "eng",
#         "Hindi": "hin",
#         "Portuguese": "por",
#         "Russian": "rus",
#         "Spanish": "spa"
#     }
#     selected_language = st.selectbox("Select your native language to speak to DataTonic", list(languages.keys()))

#     # Audio recording
#     st.write("Or record your voice:")
#     audio = mic_recorder(start_prompt="⏺️", stop_prompt="⏹️", key='recorder')

#     # Process text or audio input
#     if st.button("Process"):
#         if user_input:
#             result = asyncio.run(process_user_input(user_input))
#             st.write("Processed Result:", result)
#         elif audio:
#             # Process the audio input
#             audio_data = (audio['sample_rate'], audio['bytes'])
#             transcribed_text = speech_to_text(audio_data, languages[selected_language])
#             st.write("Transcribed Text:", transcribed_text)
            
#             # Optionally, send the transcribed text for further processing
#             result = asyncio.run(process_user_input(transcribed_text))
#             st.write("Processed Result:", result)

# if __name__ == "__main__":
#     main()

def main():
    st.title("DataTonic")
    st.subheader("🌟DataTonic: A Data-Capable AGI-style Agent Builder of Agents")

    # Input fields for project ID, region, and access token
    project_id = st.text_input("Enter your Vertex/Gemini project ID")
    region = st.text_input("Enter your Gemini Project region")
    access_token = st.text_input("Enter your Google API access token", type="password")

    # User input text
    user_input = st.text_area("Describe your request in detail with objectives and how you might achieve it:")

    # Language selection for speech-to-text
    languages = {
        "English": "eng",
        "Hindi": "hin",
        "Portuguese": "por",
        "Russian": "rus",
        "Spanish": "spa"
    }
    selected_language = st.selectbox("Select your native language to speak to DataTonic", list(languages.keys()))

    # Audio recording
    st.write("Or record your voice:")
    audio = mic_recorder(start_prompt="⏺️", stop_prompt="⏹️", key='recorder')

    # Image upload
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    # Process text, audio, or image input
    if st.button("Process"):
        combined_input = user_input

        if audio:
            # Process the audio input
            audio_data = (audio['sample_rate'], audio['bytes'])
            transcribed_text = speech_to_text(audio_data, languages[selected_language])
            st.write("Transcribed Text:", transcribed_text)
            combined_input += "\n" + transcribed_text

        if uploaded_image:
            # Process the uploaded image
            image_result = process_image(uploaded_image, project_id, region, access_token)
            st.write("Image Processing Result:", image_result)
            combined_input += "\n[Image Processed]"

        if combined_input:
            result = asyncio.run(process_user_input(combined_input))
            st.write("Processed Result:", result)

if __name__ == "__main__":
    main()