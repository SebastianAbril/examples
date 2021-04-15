import {Brand} from "../../core/brand/domain/Brand";
import {GetBrands} from "../../core/brand/application/GetBrands";

export interface onPageLoadView {
    setBrands(brands: Brand[]): void;
}

export class OnPageLoadPresenter {

    constructor(private view: onPageLoadView, private getBrands: GetBrands) {
    }

    async handle() {
        const brands = await this.getBrands.execute();
        this.view.setBrands(brands);
    }
}
