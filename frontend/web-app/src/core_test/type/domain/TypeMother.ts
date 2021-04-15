import {Type} from "../../../core/type/domain/Type";
import {UUID} from "../../../core/shared/domain/UUID";

export class TypeMother {

    static randomType(): Type {
        return {
            typeId: UUID.random(),
            name: 'Any Name'
        }
    }

    static randomTypes(number: number): Type[] {
        const types: Type[] = [];
        for (let i = 0; i < number; i++) {
            types.push(TypeMother.randomType());
        }

        return types;
    }
}
