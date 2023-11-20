from app.model.bus import Bus
from app import response
from app.utils.utils import format_array


def index():
    try:
        bus = Bus.query.all()
        data = format_array(bus)
        # print(data)
        return response.success(data, "success")
    except Exception as err:
        print("Error =>>> ", err)
