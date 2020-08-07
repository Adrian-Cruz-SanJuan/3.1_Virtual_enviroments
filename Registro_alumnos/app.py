import web

urls = (
    '/', 'application.controllers.form_registro.Registro',
)
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()