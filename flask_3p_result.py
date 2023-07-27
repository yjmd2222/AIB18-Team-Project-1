from flask import Blueprint, render_template, request, json
from weather_pd import filter_weather_data
from mangoplate_add import get_mangoplate_info

bp = Blueprint('3페이지', __name__, url_prefix='/3페이지')

@bp.route('/', methods=['GET'])
def page_3():
    start_date, end_date = request.args.get('date_range').strip('[]').replace('&#39;','').split(', ')
    region = request.args.get('region')

    weather_output = filter_weather_data(start_date, end_date)
    mangoplate_output = get_mangoplate_info(region)

    selected_output = request.args.get('input_data')

    return render_template('page3.html',
                           start_date=start_date,
                           end_date=end_date,
                           region=region,
                           weather_output=weather_output,
                           selected_output=selected_output,
                           mangoplate_output=mangoplate_output
                           )
