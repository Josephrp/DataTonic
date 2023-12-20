import sqlite3
import taskweaver
from src.TaskWeaver.taskweaver_module import TaskWeaverDataProcessor
from taskweaver.app.app import TaskWeaverApp

# Setup TaskWeaver
app_dir = "./src/taskweaver/"  # Path to the directory with taskweaver_config.json
app = TaskWeaverApp(app_dir=app_dir)
session = app.get_session()

# Function to send a message to TaskWeaver and handle the response
async def send_to_taskweaver(user_query):
    response_round = session.send_message(
        user_query,
        event_handler=lambda _type, _msg: print(f"{_type}:\n{_msg}"))
    return response_round.to_dict()

# Main function
# async def main():
#     # Existing setup (e.g., SemanticKernelDataModule initialization)
#     semantic_kernel_data_module = SemanticKernelDataModule('<google_api_key>', '<google_search_engine_id>')

#     # Example user query
#     user_query = "hello, what can you do?"
#     response = await send_to_taskweaver(user_query)
#     print(response)

if __name__ == "__main__":
    asyncio.run(main())
class TaskWeaverSQLIntegration:
    def __init__(self):
        self.taskweaver_processor = TaskWeaverDataProcessor(taskweaver.TaskWeaver())
        self.db_connection = sqlite3.connect('taskweaver_data.db')
        self.initialize_database()

    def initialize_database(self):
        self.db_connection.execute('''CREATE TABLE IF NOT EXISTS results (...);''')

    def process_and_store_data(self, task_data):

        section = task_data['section']
        details = task_data['details']
        process_function = self.kernel.Plugins.GetFunction('taskweaver', 'process_data_task')
        results = process_function(details)
        self.db_connection.execute('INSERT INTO results (section, details, processed_content) VALUES (?, ?, ?)', (section, details, results))
        self.db_connection.commit()

    def retrieve_data_for_planner(self, section):
        cursor = self.db_connection.execute('SELECT processed_content FROM results WHERE section = ?', (section,))
        return cursor.fetchone()[0]  # Assuming each section only has one entry

    def close(self):
        self.db_connection.close()
        
