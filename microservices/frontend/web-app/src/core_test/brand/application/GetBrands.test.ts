import {instance, mock, when} from "ts-mockito";
import {GetBrands} from "../../../core/brand/application/GetBrands";
import {ApiService} from "../../../core/shared/services/ApiService";
import {Brand} from "../../../core/brand/domain/Brand";
import {BrandMother} from "../domain/BrandMother";

describe('GetBrands should', () => {
    let getBrands: GetBrands;
    let apiService: ApiService;

    test('get all the brands', async () => {
        apiService = mock<ApiService>();
        getBrands = new GetBrands(instance(apiService));
        const brands = BrandMother.randomBrands(3);

        when(apiService.get<Brand[]>('/catalog/api/v1/brand/get_brands')).thenResolve(brands);

        const brandsResponse = await getBrands.execute();

        expect(brandsResponse).not.toBeUndefined();
        expect(brandsResponse).not.toBeNull();
        expect(brandsResponse.length).toBe(brands.length);
        expect(brandsResponse).toEqual(brands);
    });
});
