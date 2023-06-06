COMMANDS: dict[str: str] = {
    '/help': 'Справка по работе бота'
}

REPLIES: dict[str: str] = {
    '/help': 'Это бот поиска xml файлов на ftp. Просто введите реестровый номер документа в ЕИС.',
    'doctype_choose': 'Выберите тип документа',
    'doctypes': ['notification', 'protocol', 'contract', 'contractProcedure'],
    'notification': 'Извещения',
    'protocol': 'Протоколы',
    'contract': 'Сведения о контракте',
    'contractProcedure': 'Сведения об исполнении'
}
