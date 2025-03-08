from rio import App, Get

app = App()

@Get("/")
def home():
    return "Welcome to the Rio Frontend!"

if __name__ == "__main__":
    app.serve(port=5000, host="0.0.0.0")
