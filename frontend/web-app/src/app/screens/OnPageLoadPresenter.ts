import {Brand} from "../../core/brand/domain/Brand";
import {GetBrands} from "../../core/brand/application/GetBrands";
import {Type} from "../../core/type/domain/Type";
import {GetTypes} from "../../core/type/application/GetTypes";

export interface onPageLoadView {
    setBrands(brands: Brand[]): void;
    setTypes(types: Type[]): void;
}

export class OnPageLoadPresenter {

    constructor(
        private view: onPageLoadView,
        private getBrands: GetBrands,
        private getTypes: GetTypes
    ) {
    }

    async handle() {
        const response = await Promise.all([
            this.getBrands.execute(),
            this.getTypes.execute(),
        ]);

        this.view.setBrands(response[0]);
        this.view.setTypes(response[1]);
    }
}
