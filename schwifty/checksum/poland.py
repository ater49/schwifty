from __future__ import annotations

from typing import ClassVar

from schwifty import checksum
from schwifty.domain import Component


@checksum.register("PL")
class DefaultAlgorithm(checksum.Algorithm):
    name = "default"
    accepts: ClassVar[list[Component]] = [
        Component.BANK_CODE,
        Component.BRANCH_CODE,
    ]

    def compute(self, components: list[str]) -> str:
        weights = [3, 9, 7, 1, 3, 9, 7]
        return str(10 - checksum.weighted("".join(components), 10, weights))
