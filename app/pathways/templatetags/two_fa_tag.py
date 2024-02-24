from django import template

register = template.Library()


@register.filter(name="insert_classes")
def insert_classes(value, arg):
    the_classes = value.field.widget.attrs.get("class", "")
    if the_classes:
        the_classes = the_classes.split(" ")
    else:
        the_classes = []

    my_new_classes = arg.split(" ")

    for cs in my_new_classes:
        if cs not in the_classes:
            the_classes.append(cs)

    return value.as_widget(attrs={"class": " ".join(the_classes)})
