from schema import SampleType, SampleInput
from Model.sample import Sample
from Repository.sample import SampleRepository

class SampleService:

    @staticmethod
    async def add_sample(sample_data: SampleInput):
        sample = Sample()
        sample.name = sample_data.name
        await SampleRepository.create(sample)

        return SampleType(id=sample.id, name = sample.name)

    
    @staticmethod
    async def get_all_samples():
        list_samples = await Sample.get_all()
        return [SampleType(id=sample.id, name = sample.name) for sample in list_samples]


    @staticmethod
    async def get_sample_by_id(sample_id: int):
        sample = await SampleRepository.get_by_id(sample_id)
        return SampleType(id=sample.id, name = sample.name)
    

    @staticmethod
    async def get_vehicle_by_name(sample_name: str):
        sample = await SampleRepository.get_by_name(sample_name)
        return SampleType(id=sample.id, name = sample.name)


    @staticmethod
    async def delete(sample_id: int):
        await SampleType.delete(sample_id)
        return f"Successfully deleted data by id {sample_id}"

    
    @staticmethod
    async def update(sample_id: int, sample_data: SampleInput):
        sample = Sample()
        sample.name = sample_data.name
 
        await SampleRepository.update(sample_id, sample)

        return f"Successfully updated data by id {sample_id}"




