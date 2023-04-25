from flask import Blueprint, redirect, render_template, request, g, url_for
from blueprints.forms import QuestionForm, AnswerForm
from decorator import login_required
from exts import db
from models import QuestionModel, AnswerModel

bp =Blueprint("qa",__name__,url_prefix="/")


@bp.route("/")
def index():
    questions= QuestionModel.query.order_by(QuestionModel.create_time.desc()).all()
    return  render_template("index.html",questions=questions)

@bp.route("/qa/public",methods=["GET","POST"])
@login_required
def public_question():
    if request.method == "GET":
        return render_template("public_question.html")
    else:
        form = QuestionForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            question = QuestionModel(title=title,content=content,author=g.user)
            db.session.add(question)
            db.session.commit()
            #跳转到问答的详情页
            return redirect("/")
        else:
            print(form.errors)
            return redirect(url_for("qa.public_question"))

@bp.route("/qa/detail/<qa_id>")
def qa_detail(qa_id):
    question=QuestionModel.query.get(qa_id)
    return render_template("detail.html",question=question)

@bp.route("/answer/public",methods=["Post"])
@login_required
def public_answer():
    form=AnswerForm(request.form)
    if form.validate():
        content=form.content.data
        question_id = form.question_id.data
        answer =AnswerModel(content=content,question_id=question_id,author_id=g.user.id)
        db.session.add(answer)
        db.session.commit()
        return redirect(url_for("qa.qa_detail",qa_id=question_id))
    else:
        print(form.errors)
        return redirect(url_for("qa.qa_detail",qa_id=request.form.get("question_id")))

@bp.route("/search")
def search():
    q= request.args.get("q")
    questions =QuestionModel.query.filter(QuestionModel.title.contains(q)).all()
    return render_template("index.html",questions=questions)