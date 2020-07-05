doc = '''
#%RAML 1.0
title: python-12
mediaType: application/json
baseUri: http://localhost/python12
version: 1
protocols: [HTTPS]
securitySchemes:
  JWT:
    description: Authentication with JWT
    type: JWT
    settings:
      signatures: ['HMAC-SHA256']
    describedBy:
      headers:
        Authorization:
          type: string
      responses:
        401:
          description: {"error": "permission denied"}
types:
  Agent:
    type: object
    discriminator: agent_id
    properties:
      agent_id:
        required: true
        type: integer
      name:
        type: string
        maxLength: 50
      status:
        type: boolean
      environment:
        type: string
        maxLength: 20
      version:
        type: string
        maxLength: 5
      address:
        type: string
        maxLength: 39
      user_id:
        type: integer
    example:
      agent_id: 1
      name: Joey
      status: true
      environment: Python
      version: ex
      address: 1.1.1.1
      user_id: 1
  Auth:
    type: object
    discriminator: token
    properties:
      token: 
        required: true
        type: string
  Event:
    type: object
    discriminator: event_id
    properties:
      event_id:
        required: true
        type: integer
      level:
        type: string
        maxLength: 20
      payload:
        type: string
      shelved:
        type: boolean
      data:
        type: datetime
      agent_id:
        type: integer
    example:
      event_id: 1
      level: info
      payload: "blah"
      shelve: true
      data: 2020-07-03T00:00:00
      agent_id: 1
  Group:
    type: object
    discriminator: group_id
    properties:
      group_id:
        required: true
        type: integer
      name:
        type: string
        maxLength: 20
    example:
      name: example
      group_id: 666
  User:
    type: object
    discriminator: user_id
    properties:
      user_id:
        required: true
        type: integer
      name:
        type: string
        maxLength: 50
      email:
        type: string
        maxLength: 254
      password:
        type: string
        maxLength: 50
      last_login:
        type: date
      group_id:
        type: integer
    example:
      user_id: 1
      name: Joey
      email: joey@mail.com
      password: password
      last_login: 2020-07-03
/agents:
  get:
    description: List all agents
    securedBy: JWT
    responses:
      200: 
        body:
          application/json: 
            type: Agent[]
  post:
    description: Create Agent
    securedBy:
      - JWT
    body:
      application/json:
        type: Agent
        example:
          {"agent_id": 0,
          "name": "teste",
          "status": true,
          "environment": "teste",
          "version": "1",
          "address": "1.1.1.1",
          "user_id": 1
          }
    responses:
      201: 
        body:
          application/json:
            example: 
              Agent
      401: 
        body:
          application/json:
            {"error": "permission denied"}
  /{id}:
    get:
      description: Agent Details
      securedBy: JWT
      responses:
        200: 
          body:
            application/json: 
              Agent[]
        401: 
          body:
            application/json:
              {"error": "Permission Denied"}
        404: 
          body:
            application/json:
              {"error": "Not Found"}
    put:
      description: Update Agent
      securedBy: JWT
      responses:
        201: 
          body:
            application/json:
              Agent
        401: 
          body:
            application/json:
              {"error": "permission denied"}
        404: 
          body:
            application/json: {"error": "Bad Request"}
    delete:
      description: Delete an agent
      securedBy: JWT
      responses:
        200: 
          body:
            application/json: {"message": "Ok"}
              
        404: 
          body:
            application/json: {"error": "Bad Request"}
  /{id}/events:
    get:
      description: Get events by agent id
      securedBy: JWT
      responses:
        200: 
          body:
            application/json:
              type: Event[]
        401: 
          body:
            application/json:
              {"error": "permission denied"}
        404: 
          body:
            application/json:
              {"error": "Bad Request"}
    post:
      description: Create an event
      securedBy: JWT
      body:
        application/json:
          Event
        201: 
          body:
            application/json:
              {"message": "Ok"}
        401: 
          body:
            application/json:
              {"error": "permission denied"}
        404: 
          body:
            application/json:
              {"error": "Bad Request"}
      responses:
        201: 
          body:
            application/json:
              Event
        401: 
          body:
            application/json:
              {"error": "permission denied"}
    put:
      description: Update an event
      securedBy: JWT
      body:
        application/json: Event
        200: 
          body:
            application/json:
              {"message": "Ok"}
        401: 
          body:
            application/json:
              {"error": "permission denied"}
        404: 
          body:
            application/json:
              {"error": "Bad Request"}
      responses:
        200: 
          body:
            application/json:
              {"message": "Ok"}
        401: 
          body:
            application/json:
              {"error": "permission denied"}

    delete:
      description: Delete event
      securedBy: JWT
      body:
        application/json:
          Event
        200: 
          body:
            application/json:
              {"message": "Ok"}
        401: 
          body:
            application/json:
              {"error": "permission denied"}
      responses:
        200: 
          body:
            application/json:
              {"message": "Ok"}
        401: 
          body:
            application/json:
              {"error": "permission denied"}      
        404: 
          body:
            application/json:
              {"error": "Bad Request"}
    /{id}/events/{id}:
      get:
        description: Get event detail
        securedBy:
          - JWT
        responses:
          200: 
            body:
              application/json:
                example:
                  Event
          401: 
            body:
              application/json:
                {"error": "permission denied"}
      put:
        description: Update event
        body:
          application/json:
            type: Event
        securedBy:
          - JWT
        responses:
          200: 
            body:
              application/json:
                {"message": "Ok"}
          401: 
            body:
              application/json:
                {"error": "permission denied"}
          404:
            body:
              application/json:
                {"error": "Bad Request"}
      delete:
        description: Delete event
        securedBy:
          - JWT
        responses:
          200: 
            body:
              application/json:
                {"message": "Ok"}
          401: 
            body:
              application/json:
                {"error": "permission denied"}
/groups:
  get:
    description: Get groups list
    securedBy:
      - JWT
    responses:
      200: 
        body:
          application/json:
          type: Groups[]
      401: 
        body:
          application/json:
            {"error": "permission denied"}
      404: 
        body:
          application/json:
            {"error": "Bad Request"}
  post:
    description: Create group
    body:
      application/json:
        properties:
          Groups
        example: 
          Groups    
    securedBy:
      - JWT
    responses:
      201: 
        body:
          application/json:
            {"message": "Created"}
      401: 
        body:
          application/json:
            {"error": "permission denied"}
      404: 
        body:
          application/json:
            {"error": "Bad Request"}
  /{id}:
    get:
      description: Display group detail
      securedBy:
        - JWT
      responses:
        200: 
          body:
            application/json:
              {"message": "Ok"}
        401: 
          body:
            application/json:
              {"error": "permission denied"}
        404: 
          body:
            application/json:
              {"error": "Bad Request"}
    put:
      description: Update Group
      body:
        application/json:
          type: Groups    
      securedBy:
        - JWT
      responses:
        200: 
          body:
            application/json:
              {"message": "Ok"}
        401: 
          body:
            application/json:
              {"error": "permission denied"}
    delete:
      description: Delete group
      securedBy:
        - JWT
      responses:
        200: 
          body:
            application/json:
              {"message": "Ok"}
        401: 
          body:
            application/json:
              {"error": "permission denied"}
/users:
  get:
    description: Get users list
    securedBy:
      - JWT
    responses:
      200: 
        body:
          application/json:
            {"message": "Ok"}
      401: 
        body:
          application/json:
            {"error": "permission denied"}
  post:
    description: Create user
    body:
      application/json:
        properties:
          Users
        type: Users    
    securedBy:
      - JWT
    responses:
      201: 
        body:
          application/json:
            {"message": "Created"}
      401: 
        body:
          application/json:
            {"error": "permission denied"}
  /{id}:
    get:
      description: Get user Detail
      securedBy: JWT
      responses:
        200: 
          body:
            application/json:
              {"message": "Ok"}
        401: 
          body:
            application/json:
              {"error": "permission denied"}
        404: 
          body:
            application/json:
              {"error": "not found"}
    put:
      description: Update user
      body:
        application/json:
          type: Users    
      securedBy:
        - JWT
      responses:
        200: 
          body:
            application/json:
              {"message": "Ok"}
        401: 
          body:
            application/json:
              {"error": "permission denied"}
        404: 
          body:
            application/json:
              {"error": "Bad Request"}
    delete:
      description: Delete user
      securedBy:
        - JWT
      responses:
        200: 
          body:
            application/json:
              {"message": "Ok"}
        401: 
          body:
            application/json:
              {"error": "permission denied"}
        404: 
          body:
            application/json:
              {"error": "Bad Request"}
/auth/token:
  post:
    description: Create a token
    body:
      application/json:
        username: string
        password: string
    responses:
      201: 
        body:
          application/json:
            Auth
      400: 
        body:
          application/json:
            {"error": "auth error"}
'''
