import web

render = web.template.render('application/views/')

class Registro():

    def GET(self):
      try:
        return render.form_registro()
      except Exception as e:
        return "Error" + str(e.args)

    def POST(self):
        try:
            form = web.input()
            print(form.nombre)
            print(form.primer_a)
            print(form.segundo_a)
            print(form.edad)
            print(form.fecha_nacimiento)
            print(form.sexo)
            print(form.estado)
        except Exception as e:
            return "Error" + str(e.args)