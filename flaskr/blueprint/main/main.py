from flask import Blueprint, render_template, flash
from flaskr.blueprint.main.forms import contactForm

main_bp = Blueprint('main',__name__, template_folder='templates')

@main_bp.route('/', methods=['GET','POST'])
def index():
    form = contactForm()

    lista_cursos = ('Django','Django Rest','Flask')

    #Validacao do botao reset e enviar do formulario
    if form.validate_on_submit():
        if form.reset.data:
            print("teste1")
        elif form.enviar.data:
            print("teste2")


    return render_template('main/index.html', form=form, lista=lista_cursos)