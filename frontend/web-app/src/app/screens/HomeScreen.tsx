import {useEffect, useState} from "react";

type Brand = {
    brandId: string;
    name: string;
};

type Type = {
    typeId: string;
    name: string;
};

type Album = {
    albumId: number;
    title: string;
    url: string;
    thumbnailUrl: string;
};

const HomeScreen = () => {
    const [brands, setBrands] = useState<Brand[]>([]);
    const [types, setTypes] = useState<Type[]>([]);
    const [albums, setAlbums] = useState<Album[]>([]);

    useEffect(() => {
        const fetchData = async () => {
            const data = await Promise.all([
                fetch('/catalog/api/v1/brand/get_brands').then(response => response.json()),
                fetch('/catalog/api/v1/type/get_types').then(response => response.json()),
                fetch('https://jsonplaceholder.typicode.com/photos').then(response => response.json())
            ]);
            const brands = data[0] as Brand[];
            const types = data[1] as Type[];
            const albums = data[2].splice(0, 5) as Album[];
            setBrands(brands);
            setTypes(types);
            setAlbums(albums);
        };
        fetchData();
    }, []);

    return (
        <div style={{display:'flex', flexDirection:'column'}}>
            <div style={{display:'flex', flexDirection:'row', justifyContent:'space-between', alignItems:'center', height:'50px', padding:'0 20px 0 20px'}}>
                <label>eShop</label>
                <button>Login</button>
            </div>
            <div style={{backgroundColor:'#86C341', height:'200px'}}>a</div>
            <div style={{backgroundColor:'#28A79D', height:'50px', display:'flex', flexDirection:'row', padding:'0 0 0 30px'}}>
                <select style={{width:'100px'}}>
                    {brands.map((brand) => {
                        return (
                            <option key={brand.brandId} value={brand.brandId}>{brand.name}</option>
                        );
                    })}
                </select>
                <select style={{width:'100px'}}>
                    {types.map((type) => {
                        return (
                            <option key={type.typeId} value={type.typeId}>{type.name}</option>
                        );
                    })}
                </select>
            </div>
            <div style={{ display:'flex', justifyContent:'center'}}>
                <div style={{ display:'flex', flexWrap:'wrap', justifyContent:'space-between', maxWidth:'1000px'}}>
                    {albums.map((album) => {
                      return (
                          <div style={{
                              display:'flex',
                              flexDirection:'column',
                              border: '1px solid black',
                              alignItems:'center'

                          }}>
                              <label>{album.title}</label>
                              <img src={album.thumbnailUrl} alt={`Image for ${album.title}`} style={{width:'150px'}}/>
                          </div>
                      );
                    })};
                </div>
            </div>
        </div>
    );
};

export default HomeScreen;