def format_array(datas):
    array = []
    for i in datas:
        array.append(single_object(i))
    return array


def single_object(datas):
    data = {}
    if hasattr(datas, "bus_name"):
        data = {
            "bus_id": datas.bus_id,
            "bus_name": datas.bus_name,
            "bus_route": datas.bus_route,
            "information": datas.information,
        }
    else:
        data = {
            "id": datas.id,
            "bus_id": datas.bus_id,
            "created_at": datas.created_at,
            "category": datas.category,
        }
    return data
