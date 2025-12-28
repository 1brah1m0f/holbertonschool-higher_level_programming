#!/usr/bin/python3
"""Bu modul obyektin tipini yoxlayan funksiyanı ehtiva edir."""


def is_kind_of_class(obj, a_class):
    """
    Obyektin a_class sinfinin və ya ondan törəyən sinfin
    nümunəsi olub-olmadığını yoxlayır.

    Args:
        obj: Yoxlanılacaq obyekt.
        a_class: Yoxlanılacaq sinif.

    Returns:
        True: Əgər obj a_class-ın və ya törəməsinin nümunəsidirsə.
        False: Əks halda.
    """
    return isinstance(obj, a_class)
