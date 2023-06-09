from aiogram.filters import BaseFilter
from aiogram.types import Message


class IsEisDocNo(BaseFilter):
    """
    Реестровый номер извещения: 19 цифр, пример 0166300020623000027
    Реестровый номер протокола: 19 цифр, пример 0166300020623000027
    Реестровый номер СоК: 19 цифр, пример 3711400230023000009
    Реестровый номер СоИ: 19 цифр, пример 3711400230023000009
    """

    async def __call__(self, msg: Message):
        return len(msg.text) == 19 and msg.text.isdigit()


class IsTenderPlan2020EisDocNo(BaseFilter):
    """
    Реестровый номер ПГ: 18 цифр, пример 202301663000146002
    """

    async def __call__(self, msg: Message):
        return len(msg.text) == 18 and msg.text.isdigit()


class IsNotEisDocNo(BaseFilter):
    """
    Реестровый номер ПГ: 18 цифр, пример 202301663000146002
    Реестровый номер извещения: 19 цифр, пример 0166300020623000027
    Реестровый номер протокола: 19 цифр, пример 0166300020623000027
    Реестровый номер СоК: 19 цифр, пример 3711400230023000009
    Реестровый номер СоИ: 19 цифр, пример 3711400230023000009
    """

    async def __call__(self, msg: Message):
        return not(len(msg.text) in (18, 19) and msg.text.isdigit())
