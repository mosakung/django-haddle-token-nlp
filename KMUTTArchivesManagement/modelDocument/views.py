from django.shortcuts import render
from django.db.models import Max, F, OuterRef, Subquery, Q

from modelDocument.models import *
from modelDocument.serializers import *


class IndexingContributorController():
    def __init__(self, contributor, contributor_role, **kwargs):
        super().__init__(**kwargs)
        self.contributor = contributor
        self.contributor_role = contributor_role

    def insertFreqContributor(self):
        insertData = {
            'contributor': self.contributor,
            'contributor_role': self.contributor_role,
            'frequency': 1
        }
        serializer = IndexingContributorDocumentSerializer(data=insertData)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        print(serializer.errors)
        return False

    def updateFreqContributor(self):
        try:
            contributor = Indexing_contributor_document.objects.get(
                contributor=self.contributor)
            insertData = {
                'contributor': contributor.contributor,
                'frequency': contributor.frequency + 1
            }
            serializer = IndexingContributorDocumentSerializer(
                contributor, data=insertData)
            if serializer.is_valid():
                serializer.save()
                return serializer.data
            print(serializer.errors)
            return False
        except Indexing_contributor_document.DoesNotExist:
            return self.insertFreqContributor()
        except Indexing_contributor_document.MultipleObjectsReturned:
            print("EXCEPT : Update Indexing_contributor_document MultipleObjectsReturned")
            return False


class IndexingCreatorController():
    def __init__(self, creator, **kwargs):
        super().__init__(**kwargs)
        self.creator = creator

    def insertFreqCreator(self):
        insertData = {
            'creator': self.creator,
            'frequency': 1
        }
        serializer = IndexingCreatorDocumentSerializer(data=insertData)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        print(serializer.errors)
        return False

    def updateFreqCreator(self):
        try:
            creator = Indexing_creator_document.objects.get(
                creator=self.creator)
            insertData = {
                'creator': creator.creator,
                'frequency': creator.frequency + 1
            }
            serializer = IndexingCreatorDocumentSerializer(
                creator, data=insertData)
            if serializer.is_valid():
                serializer.save()
                return serializer.data
            print(serializer.errors)
            return False
        except Indexing_creator_document.DoesNotExist:
            return self.insertFreqCreator()
        except Indexing_creator_document.MultipleObjectsReturned:
            print("EXCEPT : Update Indexing_creator_document MultipleObjectsReturned")
            return False


class IndexingCreatorOrgnameController():
    def __init__(self, creator_orgname, **kwargs):
        super().__init__(**kwargs)
        self.creator_orgname = creator_orgname

    def insertFreqCreatorOrgname(self):
        insertData = {
            'creator_orgname': self.creator_orgname,
            'frequency': 1
        }
        serializer = IndexingCreatorOrgnameDocumentSerializer(data=insertData)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        print(serializer.errors)
        return False

    def updateFreqCreatorOrgname(self):
        try:
            creator_orgname = Indexing_creator_orgname_document.objects.get(
                creator_orgname=self.creator_orgname)
            insertData = {
                'creator_orgname': creator_orgname.creator_orgname,
                'frequency': creator_orgname.frequency + 1
            }
            serializer = IndexingCreatorOrgnameDocumentSerializer(
                creator_orgname, data=insertData)
            if serializer.is_valid():
                serializer.save()
                return serializer.data
            print(serializer.errors)
            return False
        except Indexing_creator_orgname_document.DoesNotExist:
            return self.insertFreqCreatorOrgname()
        except Indexing_creator_orgname_document.MultipleObjectsReturned:
            print(
                "EXCEPT : Update Indexing_creator_orgname_document MultipleObjectsReturned")
            return False


class IndexingPublisherController():
    def __init__(self, publisher, publisher_email, **kwargs):
        super().__init__(**kwargs)
        self.publisher = publisher
        self.publisher_email = publisher_email

    def insertFreqPublisher(self):
        insertData = {
            'publisher': self.creator_orgname,
            'publisher_email': self.publisher_email,
            'frequency': 1
        }
        serializer = IndexingPublisherDocumentSerializer(data=insertData)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        print(serializer.errors)
        return False

    def updateFreqPublisher(self):
        try:
            publisher = Indexing_publisher_document.objects.get(
                publisher=self.publisher)
            insertData = {
                'publisher': publisher.publisher,
                'frequency': publisher.frequency + 1
            }
            serializer = IndexingPublisherDocumentSerializer(
                publisher, data=insertData)
            if serializer.is_valid():
                serializer.save()
                return serializer.data
            print(serializer.errors)
            return False
        except Indexing_publisher_document.DoesNotExist:
            return self.insertFreqPublisher()
        except Indexing_publisher_document.MultipleObjectsReturned:
            print(
                "EXCEPT : Update Indexing_publisher_document MultipleObjectsReturned")
            return False


class IndexingIssuedDateController():
    def __init__(self, issued_date, **kwargs):
        super().__init__(**kwargs)
        self.issued_date = issued_date

    def insertFreqIssuedDate(self):
        insertData = {
            'issued_date': self.issued_date,
            'frequency': 1
        }
        serializer = IndexingIssuedDateDocumentSerializer(data=insertData)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        print(serializer.errors)
        return False

    def updateFreqIssuedDate(self):
        try:
            issued_date = Indexing_issued_date_document.objects.get(
                issued_date=self.issued_date)
            insertData = {
                'issued_date': issued_date.issued_date,
                'frequency': issued_date.frequency + 1
            }
            serializer = IndexingIssuedDateDocumentSerializer(
                issued_date, data=insertData)
            if serializer.is_valid():
                serializer.save()
                return serializer.data
            print(serializer.errors)
            return False
        except Indexing_issued_date_document.DoesNotExist:
            return self.insertFreqIssuedDate()
        except Indexing_issued_date_document.MultipleObjectsReturned:
            print(
                "EXCEPT : Update Indexing_issued_date_document MultipleObjectsReturned")
            return False


class DcRelationController():
    def __init__(self, Dc_relation, **kwargs):
        super().__init__(**kwargs)
        self.Dc_relation = Dc_relation

    def insertDcRelation(self, indexDocument):
        result = []
        for item in self.Dc_relation:
            insertData = {
                "DC_relation": item,
                "index_document_id": indexDocument
            }
            serializer = DcRelationSerializer(data=insertData)
            if serializer.is_valid():
                serializer.save()
                result.append(serializer.data)
            else:
                print(serializer.errors)
                result.append(False)
        return result


class DcTypeController():
    def __init__(self, Dc_type, **kwargs):
        super().__init__(**kwargs)
        self.Dc_type = Dc_type

    def insertDcType(self, indexDocument):
        result = []
        for item in self.Dc_type:
            insertData = {
                "DC_type": item,
                "index_document_id": indexDocument
            }
            serializer = DcTypeSerializer(data=insertData)
            if serializer.is_valid():
                serializer.save()
                result.append(serializer.data)
            else:
                print(serializer.errors)
                result.append(False)
        return result


class DocumentController(
        IndexingContributorController,
        IndexingCreatorController,
        IndexingCreatorOrgnameController,
        IndexingPublisherController,
        IndexingIssuedDateController,
        DcRelationController,
        DcTypeController,):
    def __init__(self, reqBody):
        self.user = reqBody.get('user')
        self.document = reqBody.get('document')

        super().__init__(
            contributor=self.document.get('DC_contributor'),
            contributor_role=self.document.get('DC_contributor_role'),
            creator=self.document.get('DC_creator'),
            creator_orgname=self.document.get('DC_creator_orgname'),
            publisher=self.document.get('DC_publisher'),
            publisher_email=self.document.get('DC_publisher_email'),
            issued_date=self.document.get('DC_issued_date'),
            Dc_relation=self.document.get('DC_relation'),
            Dc_type=self.document.get('DC_type')
        )

    def done(self, documentIndex):
        try:
            document = Document.objects.get(pk=documentIndex)
            insertData = {
                'name': document.name,
                'status_process_document': 1
            }
            serializer = DocumentSerializer(
                document, data=insertData, partial=True)
            if serializer.is_valid():
                serializer.save()
                return serializer.data
            print(serializer.errors)
            return False
        except Document.DoesNotExist:
            print("<EXCEPT> Document DoesNotExist")
            return False
        except Document.MultipleObjectsReturned:
            print("<EXCEPT> Document MultipleObjectsReturned")
            return False

    def getPathDicrectory(self):
        return self.document.get('path')

    def ask(self):
        name = self.document.get('name')
        forceAdd = self.document.get('add_version')

        if name == None:
            return False, "pls input name document"

        if forceAdd == True:
            return True, "wait add document processing (Force Version)"

        documents = Document.objects.filter(name=name)

        if not documents:
            return True, "wait add document processing"
        return False, "already document name pls change name or set add_version=True"

    def validate(self):
        name = self.document.get('name')

        documents = Document.objects.filter(name=name)
        if not documents:
            return False, 0

        current_version = documents.aggregate(Max('version'))
        rec_version = current_version['version__max']
        return True, rec_version

    def insertDocument(self):
        insertData = {
            'status_process_document': 0,
            'name': self.document.get('name'),
            'version': self.document.get('version'),
            'path': self.document.get('path'),
            'DC_title': self.document.get('DC_title'),
            'DC_title_alternative': self.document.get('DC_title_alternative'),
            'DC_description_table_of_contents': self.document.get(
                'DC_description_table_of_contents'
            ),
            'DC_description_summary_or_abstract': self.document.get(
                'DC_description_summary_or_abstract'
            ),
            'DC_description_note': self.document.get('DC_description_note'),
            'DC_format': self.document.get('DC_format'),
            'DC_format_extent': self.document.get('DC_format_extent'),
            'DC_identifier_URL': self.document.get('DC_identifier_URL'),
            'DC_identifier_ISBN': self.document.get('DC_identifier_ISBN'),
            'DC_source': self.document.get('DC_source'),
            'DC_language': self.document.get('DC_language'),
            'DC_coverage_spatial': self.document.get('DC_coverage_spatial'),
            'DC_coverage_temporal': self.document.get('DC_coverage_temporal'),
            'DC_rights': self.document.get('DC_rights'),
            'DC_rights_access': self.document.get('DC_rights_access'),
            'thesis_degree_name': self.document.get('thesis_degree_name'),
            'thesis_degree_level': self.document.get('thesis_degree_level'),
            'thesis_degree_discipline': self.document.get('thesis_degree_discipline'),
            'thesis_degree_grantor': self.document.get('thesis_degree_grantor'),
            'index_creator': self.document.get('index_creator'),
            'index_creator_orgname': self.document.get('index_creator_orgname'),
            'index_publisher': self.document.get('index_publisher'),
            'index_contributor': self.document.get('index_contributor'),
            'index_issued_date': self.document.get('index_issued_date'),
            'rec_create_by': self.document.get('rec_create_by'),
            'rec_modified_by': self.document.get('rec_create_by')
        }
        serializer = DocumentSerializer(data=insertData)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        print(serializer.errors)
        return False

    def add(self):
        status_already_document, rec_version = self.validate()
        self.document.update({"version": rec_version + 1})

        if not self.document.get('DC_contributor') == None:
            result_contributor_row = self.updateFreqContributor()
            index_contributor = result_contributor_row['indexing_contributor_id']
            self.document.update({"index_contributor": index_contributor})
        if not self.document.get('DC_creator') == None:
            result_creator_row = self.updateFreqCreator()
            index_creator = result_creator_row['indexing_creator_id']
            self.document.update({"index_creator": index_creator})
        if not self.document.get('DC_creator_orgname') == None:
            result_creator_orgname_row = self.updateFreqCreatorOrgname()
            index_creator_orgname = result_creator_orgname_row['indexing_creator_orgname_id']
            self.document.update({
                "index_creator_orgname": index_creator_orgname
            })
        if not self.document.get('DC_publisher') == None:
            result_publisher_row = self.updateFreqPublisher()
            index_publisher = result_publisher_row['indexing_publisher_id']
            self.document.update({"index_publisher": index_publisher})
        if not self.document.get('DC_issued_date') == None:
            result_issued_dater_row = self.updateFreqIssuedDate()
            index_issued_date = result_issued_dater_row['indexing_issued_date_id']
            self.document.update({
                "index_issued_date": index_issued_date
            })

        result_document_row = self.insertDocument()
        index_documnet = result_document_row['document_id']

        if not self.document.get('DC_relation') == None:
            self.insertDcRelation(index_documnet)
        if not self.document.get('DC_type') == None:
            self.insertDcType(index_documnet)

        return index_documnet


def getDocumentStatus(documentId):
    try:
        document = Document.objects.get(pk=documentId)
        serializer = DocumentSerializer(document)
        data = serializer.data
        status = data.get('status_process_document')
        return status
    except Document.DoesNotExist:
        return False
    except Document.MultipleObjectsReturned:
        return False