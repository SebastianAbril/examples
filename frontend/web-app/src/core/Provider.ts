import {GetBrands} from "./brand/application/GetBrands";
import {FetchApiService} from "./shared/services/FetchApiService";
import {ApiService} from "./shared/services/ApiService";

export class Provider {
    getBrands: GetBrands

    constructor() {
        const apiClient: ApiService = new FetchApiService();

        this.getBrands = new GetBrands(apiClient);

    }
}
