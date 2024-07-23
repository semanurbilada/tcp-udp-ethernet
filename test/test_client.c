// UDP Client driver program 
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

// Driver code 
int main() 
{ 
    char buffer[100]; 
    char *message = "Hello Server"; 
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
        printf("\n Error : Connect Failed \n"); 
        exit(0); 
    } 

    // Request to send datagram 
    sendto(sockfd, message, MAXLINE, 0, (struct sockaddr*)NULL, sizeof(servaddr)); 
    
    // Waiting for response 
    recvfrom(sockfd, buffer, sizeof(buffer), 0, (struct sockaddr*)NULL, NULL); 
    puts(buffer); 

    // Close the descriptor 
    close(sockfd); 

    return 0;
}
