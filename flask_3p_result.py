from flask import Blueprint, render_template, request, json
from weather_pd import filter_weather_data
from mangoplate_add import get_mangoplate_info

bp = Blueprint('3페이지', __name__, url_prefix='/3페이지')

def get_total_price(selected_output:dict):
    'values str->dict로 형태 변환 후 요금 합산. dict value:dict의 맨 마지막 value'
    selected_output = {k: json.loads(v.replace("'", '"')) for k,v in selected_output.items()}
    print(selected_output)
    return sum([list(item.values())[-1] for item in selected_output.values()])

@bp.route('/', methods=['GET'])
def page_3():
    start_date, end_date = request.args.get('date_range').strip('[]').replace('&#39;','').split(', ')
    region = request.args.get('region')

    weather_output = filter_weather_data(start_date, end_date)
    # mangoplate_output = get_mangoplate_info(region)

    selected_output = json.loads(request.args.get('input_data'))
    total_price = get_total_price(selected_output)

    return render_template('page3.html',
                           start_date=start_date,
                           end_date=end_date,
                           region=region,
                           weather_output=weather_output,
                        #    mangoplate_output=mangoplate_output,
                           selected_output=selected_output,
                           total_price=total_price
                           )
