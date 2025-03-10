import time
import requests

def monitoring(api_key: str, url: str):
    # Prepare the headers for the API request, including the API key
    headers = {"apikey": api_key}
    
    # Initialize variables to track the training status
    training_complete = False
    start_time = None
    elapsed_time = 0

    # Continuously check the training status until it is complete
    while not training_complete:
        time.sleep(10)  # Adjust the wait time between checks (in seconds)
    
        response = requests.get(url, headers=headers) # Send a GET request to the API
    
        if response.status_code == 200: # Check if the response status code is 200 (OK)
            data = response.json()      # Parse the response JSON data
            training_status = data["data"]["status"]  # Extract the training status
            print(f"Training status: {training_status}")
            
            if training_status == "TRAINING":
                # If training has just started, record the start time
                if start_time is None:
                    start_time = time.time()
                    print("Training started.")
            elif training_status in ["EVALUATING", "PUBLISHING"]:
                # If the training is in progress, calculate and print the elapsed time
                if start_time is not None:
                    elapsed_time = time.time() - start_time
                    print(f"Training has been in progress for {elapsed_time:.2f} seconds.")
            elif training_status == "SUCCEEDED":
                # If the training succeeded, mark it as complete and print the total training time
                training_complete = True
                if start_time is not None:
                    elapsed_time = time.time() - start_time
                print(f"Training completed successfully! Total training time: {elapsed_time:.2f} seconds.")


            elif training_status == "FAILED":
                # If the training failed, mark it as complete and notify the user
                training_complete = True
                print("Training failed. Please check the LandingLens platform for details.")

        else:
            # If the API request failed, print the error message
            print(f"Error during training status request: {response.text}")

    return elapsed_time # Return the total elapsed time for the training

