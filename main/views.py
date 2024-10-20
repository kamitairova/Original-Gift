from django.shortcuts import render

from main.models import Card, Setting, Example, Offer, Calendar, Review, Manual


def index(request):
    context = {
        'settings': Setting.objects.first(),
        'examples': Example.objects.all(),
        'offers': Offer.objects.first(),
        'calendars': Calendar.objects.all(),
        'reviews': Review.objects.all(),
        'manual': Manual.objects.first(),
        'cards': Card.objects.all(),
        # 'cards': [
        #     {
        #         'image': '../../../static/images/Group.png',
        #         'title': 'Популярное',
        #         'list': [
        #             {
        #                 'row': 'Алкоголь',
        #             },
        #             {
        #                 'row': 'Цветы',
        #             },
        #             {
        #                 'row': 'Деньги',
        #             }
        #         ],
        #         'text': 'Средний чек',
        #         'cost': 'от 1500 до 2000 ₽',
        #     },
        #     {
        #         'image': '../../../static/images/Vector.png',
        #         'title': 'Сувениры',
        #         'list': [
        #             {
        #                 'row': 'Настольные аксессуары',
        #             },
        #             {
        #                 'row': 'Картины',
        #             },
        #             {
        #                 'row': 'Статуэтки',
        #             }
        #         ],
        #         'text': 'Средний чек',
        #         'cost': 'от 1500 до 3000 ₽',
        #     },
        #     {
        #         'image': '../../../static/images/Group1.png',
        #         'title': 'Парфюмерия',
        #         'list': [
        #             {
        #                 'row': 'Крема',
        #             },
        #             {
        #                 'row': 'Туалетная вода',
        #             },
        #             {
        #                 'row': 'Гели и дезодоранты',
        #             }
        #         ],
        #         'text': 'Средний чек',
        #         'cost': 'от 1500 до 5000 ₽',
        #     },
        #     {
        #         'image': '../../../static/images/Group2.png',
        #         'title': 'Украшения',
        #         'list': [
        #             {
        #                 'row': 'Золотые украшения',
        #             },
        #             {
        #                 'row': 'Бежутерия и серебро',
        #             },
        #             {
        #                 'row': 'Изделия из камней',
        #             }
        #         ],
        #         'text': 'Средний чек',
        #         'cost': 'от 2500 ₽',
        #     },
        #     {
        #         'image': '../../../static/images/Group3.png',
        #         'title': 'Деловые аксессуары',
        #         'list': [
        #             {
        #                 'row': 'Пишущие ручки',
        #             },
        #             {
        #                 'row': 'Личные ежедневники',
        #             },
        #             {
        #                 'row': 'Кошельки, портмоне',
        #             }
        #         ],
        #         'text': 'Средний чек',
        #         'cost': 'от 1500 до 3000 ₽',
        #     },
        #     {
        #         'image': '../../../static/images/Group5.png',
        #         'title': 'Еда, сладости, деликатесы',
        #         'list': [
        #             {
        #                 'row': 'Торты',
        #             },
        #             {
        #                 'row': 'Конфеты',
        #             },
        #             {
        #                 'row': 'Деликатесы',
        #             }
        #         ],
        #         'text': 'Средний чек',
        #         'cost': 'от 500 до 2000 ₽',
        #     },
        #     {
        #         'image': '../../../static/images/Group5.png',
        #         'title': 'Еда, сладости, деликатесы',
        #         'list': [
        #             {
        #                 'row': 'Торты',
        #             },
        #             {
        #                 'row': 'Конфеты',
        #             },
        #             {
        #                 'row': 'Деликатесы',
        #             }
        #         ],
        #         'text': 'Средний чек',
        #         'cost': 'от 500 до 2000 ₽',
        #     },
        #     {
        #         'image': '../../../static/images/Group5.png',
        #         'title': 'Еда, сладости, деликатесы',
        #         'list': [
        #             {
        #                 'row': 'Торт',
        #             },
        #             {
        #                 'row': 'Конфеты',
        #             },
        #             {
        #                 'row': 'Деликатесы',
        #             }
        #         ],
        #         'text': 'Средний чек',
        #         'cost   ': 'от 500 до 2000 ₽',
        #     },
        # ]
    }
    return render(request, 'main/index.html', context)
