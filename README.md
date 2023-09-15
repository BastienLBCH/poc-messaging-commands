# Poc Messaging Service CQRS command part
This code is a proof of concept. Meaning it is not designed to be technically perfect, it is the first time I use these design patterns and I am exploring it.

It's part of an instant messaging service designed with the CQRS designed pattern combined with event sourcing.

This repo contains the command part, meaning that it takes commands and transforms it in events before sending it through Kafka.


## Installation
### Preparing
**Prerequisite :** Having docker installed

You need to create a .env file in the folder pocMessagingServiceCommands
Options are :
```
KEYCLOAK_PUBLIC_KEY
KEYCLOAK_ALG

BOOTSTRAP_SERVERS
TOPIC

ENV
```
Explaining one by one :
- **KEYCLOAK_PUBLIC_KEY**: Public key used by Keycloak to sign the JWT delivered
- **KEYCLOAK_ALG**: Algorithm used by Keycloak to sign the JWT
- **BOOTSTRAP_SERVERS**: Address of the Kafka server used to 
- **TOPIC**: Topic to send the messages on
- **ENV**: Define this variable to ENV=test for unit test purpose.

For unit test, you have to add extra variables :
```
CLIENT_ID
USERNAME_TEST
PASSWORD_TEST
```
- **CLIENT_ID**: ID of the keycloak's client used for testing purpose
- **USERNAME_TEST**: Username of a user existing for testing purpose
- **PASSWORD_TEST**: Password of a user existing for testing purpose

**Example of a complete .env file :**
```
KEYCLOAK_PUBLIC_KEY=MIIBIjANB...AQAB
KEYCLOAK_ALG=RS256

KEYCLOAK_TOKEN_URL=http://localhost:8080/realms/poc/protocol/openid-connect/token
BOOTSTRAP_SERVERS=localhost:9092
TOPIC=messaging-service

ENV=test

CLIENT_ID=test-login-client
USERNAME_TEST=John
PASSWORD_TEST=azerty
```


### Building and deploying

You can easily deploy this service using docker using these commands in the project root directory:
```bash
docker build . -t PocMessagingServiceCommandPart
```
then
```bash 
docker run -p 8000:8000 PocMessagingServiceCommandPart 
```


## Usage
This API provides endpoints to create conversations, post messages and add a participant to a conversation.


### Create a conversation
- **Endpoint**: /conversations/createconversation/
- **Method**: POST

Headers :

| Attribute       |                  Value |
|:----------------|-----------------------:|
| Authorization   |  Bearer {access token} |


Body :
(Can either be raw using the JSON syntax or a form)

| Attribute |               Value |
|:----------|--------------------:|
| name      | {conversation name} |


### Add user to a conversation
- **Endpoint**: /conversations/addparticipant/
- **Method**: POST

Headers :

| Attribute       |                  Value |
|:----------------|-----------------------:|
| Authorization   |  Bearer {access token} |


Body :
(Can either be raw using the JSON syntax or a form)

| Attribute       |                                                 Value |
|:----------------|------------------------------------------------------:|
| participant_id  |           {Id of the user to add to the conversation} |
| conversation_id | {Id of the conversation of the user has been added to |





### Send a message to a conversation
- **Endpoint**: /conversations/sendmessages/
- **Method**: POST

Headers :

| Attribute       |                  Value |
|:----------------|-----------------------:|
| Authorization   |  Bearer {access token} |


Body :
(Can either be raw using the JSON syntax or a form)

| Attribute        |                                                 Value |
|:-----------------|------------------------------------------------------:|
| message_content  |                 {Message to send to the conversation} |
| conversation_id  | {Id of the conversation of the user has been added to |







