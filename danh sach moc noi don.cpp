#include<iostream>
#include<iomanip>
#include<cstring>
using namespace std;
struct SinhVien{
	int maSV;
	char hoDem[25];
	char ten[8];
	char gioiTinh[4];
	int namSinh;
	double diemTK;
};
struct Node{
	SinhVien infor;
	Node *next;
};
typedef Node* Tro;
void create(Tro &L){
	L = NULL;
}
int empty(Tro L){
	return (L == NULL);
}
void add(Tro &L, SinhVien sv){
	Tro Q = L, P = new Node;
	P->infor = sv;
	P->next = NULL;
	if(empty(L))
		L = P;
	else{
		while(Q->next != NULL)
			Q = Q->next;
		Q->next = P;
	}
}
SinhVien taosv(int maSV, const char hoDem[25], const char ten[8], const char gioiTinh[4], int namSinh, double diemTK){
	SinhVien sv;
	sv.maSV = maSV;
	strcpy(sv.hoDem, hoDem);
	strcpy(sv.ten, ten);
	strcpy(sv.gioiTinh, gioiTinh);
	sv.namSinh = namSinh;
	sv.diemTK = diemTK;
	return sv;
}
void taods(Tro &L){
	add(L, taosv(1001,"Tran Van","Thanh","Nam",1999,7.5));
	add(L, taosv(1002,"Nguyen Thi","Huong","Nu",2000,7.3));
	add(L, taosv(1003,"Nguyen Van","Binh","Nam",1998,6.4));
	add(L, taosv(1004,"Bui Thi","Hong","Nu",2000,5.8));
	add(L, taosv(1005,"Duong Van","Giang","Nam",1998,8.3));
}
void htsv(SinhVien sv){
	cout << fixed;
	cout << setw(7) << sv.maSV;
	cout << setw(13) << left << sv.hoDem;
	cout << setw(7) << sv.ten;
	cout << setw(11) << sv.gioiTinh;
	cout << setw(10) << sv.namSinh;
	cout << setw(10) << setprecision(2) << sv.diemTK << endl;
}
void htds(Tro L){
	cout << setw(7) << left << "MaSV";
	cout << setw(13) << "Ho Dem";
	cout << setw(7) << "Ten";
	cout << setw(11) << "Gioi Tinh";
	cout << setw(10) << "Nam Sinh";
	cout << setw(10) << "Diem TK" << endl;
	Tro Q = L;
	while(Q != NULL){
		htsv(Q->infor);
		Q = Q->next;
	}
}
void xoadau(Tro &L){ 
	if (empty(L)){ 
		cout<<"Danh sach rong"; 
		return; 
	} 
	Tro Q = L; 
	L = L->next; 
	delete Q; 
}
void chenvitrithu3(Tro &L){ 
	int d = 1; 
	Tro M, Q = L; 
	while (Q != NULL && d < 3){ 
		M = Q; 
		Q = Q->next; 
		d++; 
	} 
	if (Q == NULL){ 
		cout<<"\tVi tri khong thich hop"; 
		return; 
	} 
	Tro P = new Node; 
	P->infor.maSV = 1006; 
	strcpy(P->infor.hoDem, "Le Thi"); 
	strcpy(P->infor.ten, "Doan"); 
	strcpy(P->infor.gioiTinh, "Nu"); 
	P->infor.namSinh = 1998; 
	P->infor.diemTK = 7.6; 
	P->next = M->next; 
	M->next = P; 
}
void sapxep(Tro &L){ 
	SinhVien tg; 
	Tro M, Q, R; 
	R = L; 
	while (R->next != NULL){ 
		M = R; 
		Q = R->next; 
		while (Q != NULL){ 
			if(strcmp(Q->infor.ten,M->infor.ten)<0){ 
				M = Q; 
			} 
			Q = Q->next; 
		} 
		tg = R->infor; 
		R->infor = M->infor; 
		M->infor = tg; 
		R = R->next; 
	} 
}
void xoasvthuk(Tro &L, int k){
	if (empty(L)){
		cout << "Danh sach rong";
		return;
	}
	if (k == 1) { // X�a sinh vi�n d?u ti�n
		xoadau(L);
		return;
	}
	Tro Q = L;
	int d = 1;
	while (Q != NULL && d < k - 1){
		Q = Q->next;
		d++;
	}
	if (Q == NULL || Q->next == NULL){
		cout << "Vi tri khong hop le";
		return;
	}
	Tro P = Q->next;
	Q->next = P->next;
	delete P;
}
int main(){
	Tro L;
	create(L);
	taods(L);
	htds(L);
	cout << "===========================================" << endl;
	cout << "Danh sach sinh vien sau khi xoa phan tu dau tien" << endl;
	xoadau(L);
	htds(L);
	cout << "===========================================" << endl;
	cout << "Danh sach sinh vien sau khi chen vao vi tri thu 3" << endl;
	chenvitrithu3(L);
	htds(L);
	cout << "===========================================" << endl;
	cout << "Danh sach sinh vien sau khi sap xep tang dan theo ten" << endl;
	sapxep(L);
	htds(L);
	cout << "===========================================" << endl;
	cout << "Danh sach sinh vien sau khi xoa thu 2" << endl;
	xoasvthuk(L, 2);
	htds(L);
}
