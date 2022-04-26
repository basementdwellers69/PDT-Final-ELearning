from flask import Blueprint, render_template
import sys

def construct_index_bp(controller):
    index_bp = Blueprint('index', __name__,static_folder='static',template_folder='templates')

    @index_bp.route("/")
    def index():
        # print(controller.get("id=1"), file=sys.stdout) 
        # insObj = {"status":0,
        #     "firstName":'admin',
        #     "lastName":'admin',
        #     "email":'admin@admin.com',
        #     "password":'admin',
        #     "major":1}
        # print(controller.insert(insObj), file=sys.stdout)
        return render_template('index/index.html')

    def noteboard():
        articles = controller.raw("SELECT art.id, art.title, art.body, art.user_id FROM articles art ORDER BY art.title").fetchall()

        return render_template('index/index.html', articles=articles)

    return index_bp