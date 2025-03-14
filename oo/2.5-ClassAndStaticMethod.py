class LuxuryWatch:
    __watches_created = 0
    def __init__(self):
      LuxuryWatch.__watches_created += 1

    @classmethod
    def get_number_of_watches_created(class_):
      return class_.__watches_created

    @classmethod
    def get_engraving_watch(class_, engraving: str):
      if LuxuryWatch.validate_engraving(engraving):
        watch = class_()
        watch.engraving = engraving
        return watch

    @staticmethod
    def validate_engraving(engraving: str):
      if len(engraving) < 40 and engraving.isalpha():
        return True
      raise ValueError('Unexpected value')

a = LuxuryWatch()
print(f'Number is {a.get_number_of_watches_created()}')

b = LuxuryWatch()
print(f'Number is {b.get_number_of_watches_created()}')

c = LuxuryWatch.get_engraving_watch('hahaha')
print(f'Number is { c.get_number_of_watches_created() } and engraving { c.engraving }')
