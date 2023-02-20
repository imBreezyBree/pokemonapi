from fastapi import FastAPI
from schemas import UserSignUpModel, UserSignInModel, UserResponseModel
app = FastAPI()



@app.get("/")
def printHelloWorld():
    return {"message": "Hello Code"}


@app.get("/test")
def printHelloWorld():
    return {"message": "Hello Code Test"}

@app.post("/signup", response_model=UserResponseModel)
def signup(user: UserSignUpModel):
    return {"message": "Hello Code Signup"}

@app.post("/signin", response_model=UserResponseModel)
def signin(user: UserSignInModel):
    return {"message": "Hello Code SignIn"}

@app.get("/pokemon")
def getAllPokemons():
    return {"message": "Hello Code GetAllPokemons"}


@app.put("/pokemon/{pokemon_name}")    
def updatePokemon(pokemon_name : str):
    return {"pokemon": pokemon_name}


@app.get("/pokemon/{pokemon_name}")
def getPokemon(pokemon_name : str):
    return {"pokemon": pokemon_name}

