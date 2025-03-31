from locust import HttpUser, between, task

class LoadTestUser(HttpUser):
    wait_time = between(1, 1)  # Wait time between task executions (1 second)

    @task
    def load_test(self):
        # Sending a GET request to the specified URL
        response = self.client.get("/")
        
        # Checking if the status code is 200
        assert response.status_code == 200, f"Expected status 200, but got {response.status_code}"
        
        # Checking if the response time is less than 500ms
        assert response.elapsed.total_seconds() < 0.5, f"Response time exceeded 500ms: {response.elapsed.total_seconds() * 1000} ms"
