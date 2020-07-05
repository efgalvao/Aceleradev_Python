doc = '''
#%RAML 1.0
title: Python-12
mediaType: application/json
baseUri: http://localhost/
version: 1
protocols:
  - HTTPS
securitySchemes:
  JWT:
    description: Authentication with JWT
    type: OAuth 2.0
    settings:
      signatures: ['HMAC-SHA256']
    describedBy:
      headers:
        Authorization:
          description: Use JWT for authentication
          type: string
      responses:
        401:
          description: |
              {"error": "permission denied"}
types:
  Auth:
    type: object
    discriminator: token
    properties:
      token:
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
      shelve:
        type: boolean
      date:
        type: datetime-only
      agent_id:
        type: integer
    example:
      event_id: 1
      level: info
      payload: blah
      shelve: true
      date: 2020-07-03T00:00:00
      agent_id: 1
  Group:
    type: object
    discriminator: group_id
    properties:
      group_id:
        type: integer
      name:
        type: string
        maxLength: 20
      example:
        group_id: 1
        name: devs
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
      name: zeca
      status: false
      environment: Python
      version: ex
      address: 1.1.1.1
      user_id: 1
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
      password:
        type: string
        maxLength: 50
      email:
        type: string
        maxLength: 254
      last_login:
        type: date-only
    example:
      user_id: 1
      name: Joe
      email: joe@mail.com
      password: password
      last_login: 2020-07-03
/agents:
  get:
    description: List all agents
    responses:
      200: 
        body:
          application/json:
            type: Agent[]
      401: 
        body:
          application/json:
            "permission denied"
  post:
    description: Create Agent
    securedBy:
      - JWT
    body:
      application/json:
        type: Agent
    responses:
      201: 
        body:
          application/json:
            agent
      401: 
        body:
          application/json:
            {"error": "permission denied"}
  /{id}:
    get:
      displayName: Agent Detail
      body:
        application/json:
          type: Agent
      securedBy:
        - JWT
      responses:
        200: 
          body:
            application/json:
              type: Agent
        401: 
          body:
            application/json:
              {"error": "permission denied"}
        404: 
          body:
            application/json:
              {"error": "not found"}
    put:
      description: Update Agent
      body:
        application/json:
          type: Agent
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
      description: Delete agent
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
  /{id}/events:
    get:
      description: Get events by agent id
      securedBy:
        - JWT
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
      description: Create event
      body:
        application/json:
          type: Event
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
                  {"message": "Ok"}
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
        type: Groups    
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
/auth/token:
  post:
    description: Get token for authentication
    body:
      application/json:
        type: Auth    
    body:
      application/json:
        username: string
        password: string
    responses:
      200: 
        body:
          application/json:
            Auth
      401: 
        body:
          application/json:
            {"error": "permission denied"}
'''
