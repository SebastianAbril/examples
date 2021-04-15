import {ApiService} from "../../shared/services/ApiService";
import {Brand} from "../domain/Brand";

export class GetBrands {
    constructor(private apiClient: ApiService) {
    }

    execute(): Promise<Brand[]> {
        return this.apiClient.get<Brand[]>('/catalog/api/v1/brand/get_brands');
    }
}
