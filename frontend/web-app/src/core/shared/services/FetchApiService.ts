import {ApiService} from "./ApiService";

export class FetchApiService implements  ApiService{
    get<T>(url: string): Promise<T> {
        return fetch(url).then(response => response.json())
    }
}
