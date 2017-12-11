import json

filename = "topic_data2"
temp_list = []

with open(filename) as f_obj:
    data = f_obj.readlines()

    for d in data:
        string = d.lstrip("b")
        string = string.strip()

        # Need to refactor the following into function.
        string = string.replace("{", "")
        string = string.replace("}", "")
        string = string.replace("[", "")
        string = string.replace("]", "")
        string = string.replace("'", "")
        string = string.replace(" ", "")
        string = string.replace('"', "")

        # Add your checks with the following style. These fields
        # might or might not be excess. Excess fields are deleted.
        a = "rxInfo:"
        b = "txInfo:"
        c = "dataRate:"
        if a in string:
            string = string.replace(a, "")
        if b in string:
            string = string.replace(b, "")
        if c in string:
            string = string.replace(c, "")

        # Generate formatted dictionary and write it to file.
        new_dict = dict(a.split(":", 1) for a in string.split(","))
        temp_list.append(new_dict)

with open("formatted_topic2.json", "a") as f_obj_2:
    json.dump(temp_list, f_obj_2)
