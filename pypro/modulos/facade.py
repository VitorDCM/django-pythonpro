from typing import List

from pypro.modulos.models import Modulo, Aula


def listar_modulos_ordenados() -> List[Modulo]:
    """
    Lista modulos ordenados por titulos.
    :return:
    """

    return list(Modulo.objects.order_by('order').all())


def encontrar_modulo(slug: str) -> Modulo:
    """
    Retorna um objeto do tipo Modulo a partir do seu slug.

    @param slug:
    @return: Modulo
    """
    return Modulo.objects.get(slug=slug)


def listar_aulas_de_modulo_ordenadas(modulo: Modulo) -> List[Modulo]:
    """
    Retorna uma lista de modulos que contem aulas.

    @param modulo:
    @return:list[Modulo]
    """

    return list(modulo.aula_set.order_by('order').all())


def encontrar_aula(slug: str) -> Aula:
    """
    Retorna um objeto do tipo Aula a partir do seu slug.

    @param slug:
    @return: Aula
    """
    return Aula.objects.get(slug=slug)
