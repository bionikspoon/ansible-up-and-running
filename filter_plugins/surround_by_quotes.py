def surround_by_quote(items):
    return ['"%s"' % item for item in items]


class FilterModule(object):
    def filters(self):
        return {'surround_by_quote': surround_by_quote}
