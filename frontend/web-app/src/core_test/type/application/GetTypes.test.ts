import {GetTypes} from "../../../core/type/application/GetTypes";
import {ApiService} from "../../../core/shared/services/ApiService";
import {instance, mock, when} from "ts-mockito";
import {TypeMother} from "../domain/TypeMother";


describe('GetTypes should', () => {
    let getTypes: GetTypes
    let apiService: ApiService;

    test('get all the type', async () => {
        apiService= mock<ApiService>();
        getTypes = new GetTypes(instance(apiService));

        const randomTypes = TypeMother.randomTypes(3);

        when(apiService.get('/catalog/api/v1/type/get_types')).thenResolve(randomTypes);

        const types = await getTypes.execute();

        expect(types).toEqual(randomTypes);

    })
});
