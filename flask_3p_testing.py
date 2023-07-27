from flask import Blueprint, render_template, request, json
from heejae_weather import main

bp = Blueprint('3페이지', __name__, url_prefix='/3페이지')

@bp.route('/', methods=['GET'])
def page_3():
    start_date, end_date = request.args.get('date_range').strip('[]').replace('&#39;','').split(', ')
    print(start_date,end_date)
    output = main(start_date, end_date)

    selected_data = request.args.get('input_data')

    return render_template('output.html', start_date=start_date, end_date=end_date, output=output, selected_data=selected_data)
