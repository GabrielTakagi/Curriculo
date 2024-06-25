from flask import Blueprint, render_template, flash
from flaskr.blueprint.main.forms import contactForm

main_bp = Blueprint('main',__name__, template_folder='templates')

# Pagina inicial
@main_bp.route('/', methods=['GET','POST'])
def index():
    form = contactForm()

    lista_formacoes = ('Tecnico em TI', 'Ciência da Computação')
    lista_cursos = ('Django','Django Rest','Flask')

    #Validacao do botao reset e enviar do formulario
    if form.validate_on_submit():
        if form.reset.data:
            print("teste1")
        elif form.enviar.data:
            print("teste2")

    return render_template('main/index.html', form = form, lista_cursos = lista_cursos, lista_formacoes = lista_formacoes)


@main_bp.route('/formacao/<nome>')
def formacao(nome):
    return render_template('main/formacao.html', nome=nome)

@main_bp.route('/curso/<nome>')
def curso(nome):
    return render_template('main/formacao.html', nome=nome)