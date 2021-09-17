import {GetBrands} from "./brand/application/GetBrands";
import {FetchApiService} from "./shared/services/FetchApiService";
import {ApiService} from "./shared/services/ApiService";
import {GetTypes} from "./type/application/GetTypes";

export class Provider {
    getBrands: GetBrands;
    getTypes: GetTypes;

    constructor() {
        const apiClient: ApiService = new FetchApiService();

        this.getBrands = new GetBrands(apiClient);
        this.getTypes = new GetTypes(apiClient);

    }
}
