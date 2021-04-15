import {Brand} from "../../../core/brand/domain/Brand";
import {v4 as uuidv4} from 'uuid';

export class BrandMother {

    static random_brand(): Brand {
        return {
            brandId: uuidv4(),
            name: 'Any Brand'
        };
    }

    static random_brands(quantity: number): Brand[] {
        const brands: Brand[] = [];
        for (let i = 0; i < quantity; i++) {
            brands.push(BrandMother.random_brand());
        }

        return brands;
    }
}
