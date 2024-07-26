#include <stdio.h> 
#include <strings.h> 
#include <sys/types.h> 
#include <arpa/inet.h> 
#include <sys/socket.h> 
#include <netinet/in.h> 

#define PORT 5000 
#define MAXLINE 1000 

int main() 
{ 
    char buffer[100]; 
    char *message = "Hello Client"; 
    int listenfd, len; 
    struct sockaddr_in servaddr, cliaddr; 
    bzero(&servaddr, sizeof(servaddr)); 

    // Create a UDP Socket 
    listenfd = socket(AF_INET, SOCK_DGRAM, 0); 
    servaddr.sin_addr.s_addr = htonl(INADDR_ANY); 
    servaddr.sin_port = htons(PORT); 
    servaddr.sin_family = AF_INET; 

    // Bind server address to socket descriptor 
    bind(listenfd, (struct sockaddr*)&servaddr, sizeof(servaddr)); 
    
    // Receive the datagram 
    len = sizeof(cliaddr); 
    while (1) 
    { 
        int n = recvfrom(listenfd, buffer, sizeof(buffer), 0, (struct sockaddr*)&cliaddr, (socklen_t*)&len); // Receive message from client 
        buffer[n] = '\0'; 
        printf("Client message: %s\n", buffer); 
        
        // Send the response 
        sendto(listenfd, message, MAXLINE, 0, (struct sockaddr*)&cliaddr, sizeof(cliaddr)); 
    }

    return 0;
}
