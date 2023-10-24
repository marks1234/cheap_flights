package main

import (
	"fmt"
	"io"
	"net/http"
)

func main() {
	// Replace with your Amadeus API key
	apiKey := "NhOQ7AAh3Rqhr3BbDLVYtUP4ZHIV"

	// Define the API endpoint URL
	endpoint := "https://test.api.amadeus.com/v1/shopping/flight-destinations?origin=MAD"

	// Construct the request URL with query parameters
	req, err := http.NewRequest("GET", endpoint, nil)
	if err != nil {
		fmt.Println("Error creating request:", err)
		return
	}

	// Set the API key in the request headers
	req.Header.Add("Authorization", "Bearer "+apiKey)

	// Create an HTTP client and send the request
	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Println("Error sending request:", err)
		return
	}
	defer resp.Body.Close()

	// Read and print the response
	body, err := io.ReadAll(resp.Body)
	if err != nil {
		fmt.Println("Error reading response:", err)
		return
	}

	fmt.Println(string(body))
}
