import actions from './actions';
import mutations from './mutations';
import getters from './getters';

const defaultState = {
    trustedPeopleData:
        [
            {
                name: 'A',
                imageList: []
            },
            {
                name: 'B',
                imageList: []
            },
            {
                name: 'C',
                imageList: []
            },
        ],
    newPersonData: {
        name: '',
        imageList: []
    }
};

export default {
    state: defaultState,
    actions,
    mutations,
    getters
};
