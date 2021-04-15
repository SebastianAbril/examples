import {Brand} from "../../../core/brand/domain/Brand";
import {UUID} from "../../../core/shared/domain/UUID";

export class BrandMother {

    static randomBrand(): Brand {
        return {
            brandId: UUID.random(),
            name: 'Any Brand'
        };
    }

    static randomBrands(number: number): Brand[] {
        const brands: Brand[] = [];
        for (let i = 0; i < number; i++) {
            brands.push(BrandMother.randomBrand());
        }

        return brands;
    }
}
