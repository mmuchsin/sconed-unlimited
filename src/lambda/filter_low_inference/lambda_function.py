import json


THRESHOLD = .7


def lambda_handler(event, context):
    
    # Grab the inferences from the event
    inference_bicycle, inference_motorcycle = event["body"]["inferences"]  ## TODO: fill in
    
    # Check if any values in our inferences are above THRESHOLD
    meets_threshold = (inference_bicycle >= THRESHOLD) or (inference_motorcycle >= THRESHOLD) ## TODO: fill in
        
    
    # If our threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if meets_threshold:
        pass
    else:
        raise Exception("THRESHOLD_CONFIDENCE_NOT_MET")    
        
    return {
                'statusCode': 200,
                'body': json.dumps(event)
            } 