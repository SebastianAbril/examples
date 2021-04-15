import {Type} from "../domain/Type";
import {ApiService} from "../../shared/services/ApiService";

export class GetTypes {
    constructor(private apiService: ApiService) {
    }

    execute(): Promise<Type[]> {
        return this.apiService.get<Type[]>('/catalog/api/v1/type/get_types');
    }
}
