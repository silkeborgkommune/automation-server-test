import asyncio

import logging
import sys

from automation_server_client import AutomationServer, Workqueue, WorkItemError, Credential, WorkItemStatus


async def populate_queue(workqueue: Workqueue):
    logger = logging.getLogger(__name__)

    logger.info("Hello from populate workqueue!")
    print("Hello from populate workqueue!")

    # List of names to post sequentially
    names = [
        "sofie", 
        "jacob", 
        "mark"
        ]

    # Loop to create and post JSON items sequentially from the list
    for i, name in enumerate(names):
        # Create the data object as a string
        data = {
            "name": name
        }
       
        try:
            workqueue.add_item(data=data, reference=name)
        except Exception as e:
            print(f"An error occurred while posting item {i+1}: {e}")


#async def process_workqueue(workqueue: Workqueue):
 #   logger = logging.getLogger(__name__)

 #   logger.info("Hello from process workqueue!")


# Run the async main function
if __name__ == "__main__":
    ats = AutomationServer.from_environment()
    workqueue = ats.workqueue()

    # Database connection parameters
    #database_RPA_OEKIT_credential = Credential.get_credential("Database-RPA_OEKIT")

 # Queue management
    if "--queue" in sys.argv:
        workqueue.clear_workqueue(WorkItemStatus.NEW)
        asyncio.run(populate_queue(workqueue))
        exit(0)

    # Process workqueue
    # asyncio.run(process_workqueue(workqueue))