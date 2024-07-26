#include <stdio.h> 
#include <strings.h> 
#include <sys/types.h> 
#include <arpa/inet.h> 
#include <sys/socket.h> 
#include <netinet/in.h> 
#include <unistd.h> 
#include <stdlib.h> 

#define PORT 5000 
#define MAXLINE 1000 
// change for higher value of messages
#define MESSAGE_COUNT 100

int main() 
{ 
    char buffer[100]; 
    char message[100]; 
    int sockfd, n; 
    struct sockaddr_in servaddr; 
    
    // Clear servaddr 
    bzero(&servaddr, sizeof(servaddr)); 
    servaddr.sin_addr.s_addr = inet_addr("server_ip"); 
    servaddr.sin_port = htons(PORT); 
    servaddr.sin_family = AF_INET; 
    
    // Create datagram socket (udp)
    sockfd = socket(AF_INET, SOCK_DGRAM, 0); 
    
    // Connect to server 
    if (connect(sockfd, (struct sockaddr *)&servaddr, sizeof(servaddr)) < 0) 
    { 
        printf("\nError: Connect Failed\n"); 
        exit(0); 
    } 

    // Request to send datagram 
    for (int i = 0; i < MESSAGE_COUNT; i++) 
    { 
        snprintf(message, sizeof(message), "Message %d: Hello Server", i+1); 
        sendto(sockfd, message, MAXLINE, 0, (struct sockaddr*)NULL, sizeof(servaddr)); 
        
        // Waiting for response 
        recvfrom(sockfd, buffer, sizeof(buffer), 0, (struct sockaddr*)NULL, NULL); 
        printf("Server response: %s\n", buffer); 
    }

    // Close the descriptor 
    close(sockfd); 

    return 0;
}
