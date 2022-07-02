from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=255)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

    @staticmethod
    def get_child(menus, parent):
        list = {}
        childs = menus.filter(parent__id=parent)
        for child in childs:
            list[child.title] = {
                'id': child.id,
                'childs': Menu.get_child(menus, child.id)
            }
        return list if list else None

    @staticmethod
    def get_tree():
        menus = Menu.objects.all()
        root = 0
        return Menu.get_child(menus, root)

    @staticmethod
    def get_list():
        return list(Menu.objects.values('id', 'title', 'parent__id'))
